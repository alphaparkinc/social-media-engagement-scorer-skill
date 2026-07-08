"""
social-media-engagement-scorer-skill: Client SDK
Estimates social post reach score based on text formatting anchors.
"""
from __future__ import annotations
from typing import Optional


class SocialMediaEngagementScorerClient:
    """
    SDK for content viral-factor analysis.
    """

    def score_post(self, post_copy: str, has_images: bool) -> dict:
        score = 3.0
        sugs = []

        if has_images:
            score += 3.0
        else:
            sugs.append("Add an image or video asset to increase reach rate by up to 100%.")

        # Formatting audit
        if "#" in post_copy:
            score += 1.5
        else:
            sugs.append("Include 2-3 relevant hashtags to boost search indexing.")

        if len(post_copy) > 200:
            score -= 1.0
            sugs.append("Keep copy short (under 150 chars) for better readability.")
        else:
            score += 1.5

        final_score = round(max(0.1, min(10.0, score)), 1)

        return {
            "engagement_score": final_score,
            "suggestions": sugs
        }
