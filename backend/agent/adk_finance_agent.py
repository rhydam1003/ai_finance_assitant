from google.adk.agents import Agent

from tools.adk_tools import (
    add_expense,
    create_budget,
    get_budget_summary,
    spending_analysis
)

root_agent = Agent(
    name="finance_agent",

    model="gemini-2.5-flash",

    description="AI Financial Assistant",

    instruction="""
You are a smart financial assistant.

Available tools:

1. add_expense
   Use when user records spending.

Examples:
- I spent 500 on Swiggy
- Paid 200 for coffee
- Spent 1000 on groceries

2. create_budget
   Use when user sets a budget.

Examples:
- Set my food budget to 5000
- My transport budget is 3000

3. get_budget_summary
   Use when user asks:
   - Show my budget summary
   - How much budget is left?
   - Budget status

4. spending_analysis
   Use when user asks:
   - Analyze my spending
   - Where do I spend most money?
   - Spending insights

Always call the appropriate tool.
""",

    tools=[
        add_expense,
        create_budget,
        get_budget_summary,
        spending_analysis
    ]
)