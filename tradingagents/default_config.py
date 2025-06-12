import os

DEFAULT_CONFIG = {
    'project_dir': os.path.abspath(os.path.join(os.path.dirname(__file__), '.')),
    'data_dir': '/Users/yluo/Documents/Code/ScAI/FR1-data',
    'data_cache_dir': os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '.')),
        'dataflows/data_cache',
    ),
    # LLM settings
    'deep_think_llm': {
        'provider': 'gemini',
        'model': 'gemini-2.0-flash',
        'temperature': 0.7,
    },
    'quick_think_llm': {
        'provider': 'gemini',
        'model': 'gemini-2.0-flash',
        'temperature': 0.1,
    },
    # Provider-specific settings
    'openrouter': {'base_url': 'https://openrouter.ai/api/v1'},
    'gemini': {'google_api_key': os.getenv('GOOGLE_API_KEY', '')},
    # Debate and discussion settings
    'max_debate_rounds': 1,
    'max_risk_discuss_rounds': 1,
    'max_recur_limit': 100,
    # Tool settings
    'online_tools': True,
}
