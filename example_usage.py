"""
example_usage.py -- Demonstrates SocialMediaEngagementScorerClient
"""
from client import SocialMediaEngagementScorerClient

def main():
    client = SocialMediaEngagementScorerClient()
    result = client.score_post(
        post_copy="This new serum is amazing! Find yours here today.",
        has_images=False
    )
    print("[Post Scorer Result]")
    print(f"Engagement Score: {result['engagement_score']}/10.0")
    print(f"Suggestions: {result['suggestions']}")

if __name__ == "__main__":
    main()
