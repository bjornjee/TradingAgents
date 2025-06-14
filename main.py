from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config['max_debate_rounds'] = 1  # Increase debate rounds
config['online_tools'] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(selected_analysts=['market'], debug=True, config=config)

# forward propagate
_, decision = ta.propagate('DVA', '2025-06-13')
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
