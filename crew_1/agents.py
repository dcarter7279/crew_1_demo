from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset

class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="Conduct thorough research on people and companies involved in the meeting",
            tools=ExaSearchToolset.tools(self),
            backstory=dedent("""\
            As a Research Specialist, your mission is to uncover detailed information
            about the individuals and entities participating in the meeting. Your insights
            will lay the groundwork for strategic meeting preparation."""),
            verbose=True
        )

    def industry_analysis_agent(self):
        return Agent(
            role="Industry Analysis",
            goal="Analyze the current industry trends, challenges, and opportunities",
            tools=ExaSearchToolset.tools(self),
            backstory=dedent("""\
            As an Industry Analysis, your analysis will identify key trends, challenges
            facing the industry, and potential opportunities that could be leveraged during the 
            meeting for strategic advantage."""),
            verbose=True
        )

    def meeting_strategy_agent(self):
        return Agent(
            role="Meeting Strategy Analysis",
            goal="Develop talking points, questions, and strategic angles for the meeting",
            tools=[],
            backstory=dedent("""\
            As a Strategy Advisor, your expertise will guide the development of talking points,
            insightful questions, and strategic angles to ensure the meeting's objectives are 
            achieved."""),
            verbose=True
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role="Briefing Coordinator",
            goal="Compile all gathered information into a concise, informative briefing document",
            tools=[],
            backstory=dedent("""\
            As the Briefing Coordinator, your role is to consolidate the research, analysis,
            and strategic insights."""),
            verbose=True
        )
