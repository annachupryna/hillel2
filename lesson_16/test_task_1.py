from lesson_16.task_1 import TeamLead


def test_team_lead_inherits_manager_attributes():
    team_lead = TeamLead('Olena', 2700, 'qa', 'python', 7)
    assert hasattr(team_lead, 'department'), "TeamLead не успадковує атрибут 'department'"
    assert team_lead.department == 'qa'


def test_team_lead_inherits_developer_attributes():
    team_lead = TeamLead('Olena', 2700, 'qa', 'python', 7)
    assert hasattr(team_lead, 'programming_language'), "TeamLead не успадковує атрибут 'programming_language'"
    assert team_lead.programming_language == 'python'
