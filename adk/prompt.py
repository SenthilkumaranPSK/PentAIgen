# prompt.py

# Prompts for Wealth Strategist tools
WEALTH_STRATEGIST_PROMPTS = [
    "What's my current net worth?",  # Triggers get_net_worth()
    "Can you give me an update on my financial goals?",  # Triggers get_goals_status()
    "Project my net worth for the next 5 years.",  # Triggers simulate_projection(years=5)
    "I'd like to see my assets and liabilities.",  # Triggers get_net_worth()
    "How am I doing on my retirement savings?",  # Triggers get_goals_status()
    "What if I save more? Can you simulate my net worth projection for 10 years?",  # Triggers simulate_projection(years=10)
]

# Prompts for Portfolio Manager tools
PORTFOLIO_MANAGER_PROMPTS = [
    "What are my current investment holdings?",  # Triggers get_holdings()
    "Show me my stock transactions from last month.",  # Triggers get_transactions(asset_type='stock', date_range='last month')
    "How are my mutual funds performing?",  # Triggers get_asset_performance(asset_type='mutual funds')
    "Can I see a list of all my FDs?",  # Triggers get_holdings()
    "I need a record of my gold transactions for the year 2024.",  # Triggers get_transactions(asset_type='gold', date_range='2024')
    "What's the XIRR for my entire portfolio?",  # Triggers get_asset_performance(asset_type='all')
]

# Prompts for Tax Optimizer tools
TAX_OPTIMIZER_PROMPTS = [
    "What are my income sources?",  # Triggers get_income_sources()
    "Can you get my tax documents?",  # Triggers get_tax_documents()
    "What tax deductions am I eligible for this year?",  # Triggers get_eligible_deductions()
    "I need a summary of my salary and dividend income.",  # Triggers get_income_sources()
    "Fetch my Form 16 and 26AS data.",  # Triggers get_tax_documents()
    "Tell me about available tax-saving instruments.",  # Triggers get_eligible_deductions()
]

# Combine all into one list (optional)
ALL_PROMPTS = WEALTH_STRATEGIST_PROMPTS + PORTFOLIO_MANAGER_PROMPTS + TAX_OPTIMIZER_PROMPTS
