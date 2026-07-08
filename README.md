# social-media-engagement-scorer-skill

> **GenPark AI Agent Skill** -- Social copy engagement analyzer.

## Quick Start

```python
from client import SocialMediaEngagementScorerClient
client = SocialMediaEngagementScorerClient()
res = client.score_post("Check out our new stock! #activewear", True)
print(res["engagement_score"])
```
