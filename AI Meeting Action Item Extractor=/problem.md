# Problem
Given a meeting transcript, automatically extract:
Action Items
Assignee
Due Date
Priority

# Input
 Rahul: I'll complete authentication by Friday.
 Priya: I will prepare API documentation before Monday.
 Manager: Urgent, deployment must happen by tomorrow.
# Output

[
{
assignee: Rahul,
task: Complete authentication,
dueDate: Friday,
priority: Medium
},
{
assignee: Priya,
task: Prepare API documentation,
dueDate: Monday,
priority: Medium
},
{
assignee: Team,
task: Deployment
dueDate: Tomorrow,
priority: High
}
]
# Features
# Phase 1
Extract names
Extract tasks
Extract deadlines
# Phase 2
Priority Detection
Urgent keyword analysis
Task categorization
# Phase 3
AI Integration
OpenAI API
Gemini API
