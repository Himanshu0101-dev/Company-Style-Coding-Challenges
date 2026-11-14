class InterviewScheduler:

    def __init__(self):
        self.schedule = []

    def assign_interviews(self, interviewers, candidates):

        assigned_candidates = set()

        for interviewer, interviewer_slots in interviewers.items():

            for slot in interviewer_slots:

                for candidate, candidate_slots in candidates.items():

                    if candidate in assigned_candidates:
                        continue

                    if slot in candidate_slots:

                        self.schedule.append(
                            (interviewer, candidate, slot)
                        )

                        assigned_candidates.add(candidate)
                        break

        return self.schedule


interviewers = {
    "A": ["10-11", "2-3", "3-4"],
    "B": ["9-10", "11-12"]
}

candidates = {
    "C1": ["10-11"],
    "C2": ["11-12"],
    "C3": ["2-3"],
    "C4": ["9-10"]
}

scheduler = InterviewScheduler()

result = scheduler.assign_interviews(
    interviewers,
    candidates
)

print("Interview Schedule:")

for interviewer, candidate, slot in result:
    print(
        f"{interviewer} -> {candidate} at {slot}"
    )
