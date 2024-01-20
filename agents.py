import os
import openai
from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.agents import load_tools

openai.api_key = os.getenv("OPENAI_API_KEY")

class MarketingAnalysisAgents:
	def __init__(self):
		self.llm = None  # We will use OpenAI's API directly

	def product_competitor_agent(self):
		return Agent(
			role="Lead Market Analyst",
			goal=dedent("""\
				Conduct an analysis of the product's competitors, providing in-depth insights to guide marketing strategies."""),
			backstory=dedent("""\
					You are an expert market analyst abd are adept at predicting market trends and behaviors."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet
			],
			allow_delegation=False,
			llm=self.llm,
			verbose=True
		)

	def _ask_openai(self, prompt, max_tokens=150):
		response = openai.Completion.create(
			engine="text-davinci-003",
			prompt=prompt,
			max_tokens=max_tokens
		)
		return response.choices[0].text.strip()

	def strategy_planner_agent(self):
		return Agent(
			role="Chief Marketing Strategist",
			goal=dedent("""\
				Provide comprehensive advice and solutions for various digital marketing challenges and queries."""),
			backstory=dedent("""\
				As the Chief Marketing Strategist, you expertly blend data-driven analysis, innovative digital marketing techniques, 
				and dynamic leadership to steer a company towards market dominance and lasting brand resonance."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_instagram
			],
			llm=self.llm,
			verbose=True
		)

	def creative_content_creator_agent(self):
		return Agent(
			role="Creative Content Creator",
			goal=dedent("""\
				Develop compelling and innovative content
				for an inbound seo ad campaign, with a focus on creating
				high-impact product blog that tie the products features to current industry pains."""),
			backstory=dedent("""\
				As a Creative Content Creator at a top-tier
				digital marketing agency, you excel in crafting narratives
				that resonate with audiences.
				Your expertise lies in turning marketing strategies
				into engaging stories and visual content that capture
				attention and inspire action."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_instagram
			],
			llm=self.llm,
			verbose=True
		)

	def senior_photographer_agent(self):
		return Agent(
				role="Senior Photographer",
				goal=dedent("""\
					Take the most amazing photographs for blog articles that
					capture emotions and convey a compelling message."""),
				backstory=dedent("""\
					As a Senior Photographer at a leading digital marketing
					agency, you are an expert at taking amazing photographs that
					inspire and engage, you're now working on a new campaign for a super
					important customer and you need to take the most amazing photograph."""),
				tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_instagram
				],
				llm=self.llm,
				allow_delegation=False,
				verbose=True
		)

	def chief_creative_diretor_agent(self):
		return Agent(
				role="Chief Creative Director",
				goal=dedent("""\
					Oversee the work done by your team to make sure it's the best
					possible and aligned with the product's goals
					Review, approve, ask clarifying question or delegate follow up work as 
					needed to make sure your team is making the best decisions"""),
				backstory=dedent("""\
					You're the Chief Content Officer of leading digital
					marketing agency specialized in product branding. 
					You're working with a new customer's project, and you are trying to make sure 
					your team is crafting the best possible	content."""),
				tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_instagram
				],
				llm=self.llm,
				verbose=True
		)
