import datetime
import typing as T
from dataclasses import dataclass

import dateutil.parser
import requests

DATE_FORMAT = "%d.%m.%Y"


@dataclass
class Worklog:
    id: T.Optional[int]
    date: datetime.date
    duration: datetime.timedelta
    description: str
    project_id: int
    ticket: str


class IntranetApi:
    def __init__(self, user_id: int, session_id: str) -> None:
        self.user_id = user_id
        self.session = requests.session()
        self.session.headers.update(
            {"Cookie": f"beaker.session.id={session_id}"}
        )

        response = self.session.get(
            "https://intranet.stxnext.pl/api/projects",
        )
        response.raise_for_status()
        self.projects = response.json()["projects"]

    def get_project_id_by_name(self, name: str) -> T.Optional[int]:
        for project in self.projects:
            if project["name"] == name:
                return project["id"]
        return None

    def get_worklogs(
        self, start: datetime.date, end: datetime.date
    ) -> T.Iterable[Worklog]:
        response = self.session.get(
            "https://intranet.stxnext.pl/api/user_times",
            params={
                "user_id": self.user_id,
                "start_date": start.strftime(DATE_FORMAT),
                "end_date": end.strftime(DATE_FORMAT),
            },
        )
        response.raise_for_status()
        data = response.json()

        for entry in sorted(data, key=lambda entry: entry["id"]):
            project_id = self.get_project_id_by_name(
                entry["project"]["client_name"]
                + " / "
                + entry["project"]["project_name"]
            )

            assert project_id

            yield Worklog(
                id=entry["id"],
                date=datetime.datetime.strptime(
                    entry["date"], DATE_FORMAT
                ).date(),
                duration=datetime.timedelta(hours=entry["time"]),
                description=entry["desc"],
                project_id=project_id,
                ticket=entry["ticket_id"],
            )

    def create_worklog(self, worklog: Worklog) -> None:
        data = self._serialize_worklog(worklog)
        response = self.session.post(
            "https://intranet.stxnext.pl/api/user_times", json=data
        )
        response.raise_for_status()

    def update_worklog(self, worklog: Worklog) -> None:
        data = self._serialize_worklog(worklog)
        response = self.session.put(
            f"https://intranet.stxnext.pl/api/user_times/{worklog.id}",
            json=data,
        )
        response.raise_for_status()

    def delete_worklog(self, worklog_id: int) -> None:
        response = self.session.delete(
            f"https://intranet.stxnext.pl/api/user_times/{worklog_id}"
        )
        response.raise_for_status()

    def _serialize_worklog(self, worklog: Worklog) -> T.Any:
        payload = {
            "user_id": self.user_id,
            "description": worklog.description,
            "project_id": worklog.project_id,
            "date": worklog.date.strftime(DATE_FORMAT),
            "time": worklog.duration.total_seconds() / 3600.0,
        }
        if worklog.ticket:
            payload["ticket_id"] = worklog.ticket
        return payload
