from ui.console import Console
from logic.controller import Controller
from repository.studentRepo import StudentRepo, FileStudentRepo


def main():
    console = Console(Controller(FileStudentRepo('students.dat')))
    console.run()


main()
