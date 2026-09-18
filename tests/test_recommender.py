from src.hairstyle_recommender import HairstyleRecommender


def test_oval_recommendations():
    recommender = HairstyleRecommender()

    results = recommender.get_recommendations("oval")

    assert len(results) > 0
    assert "Layered Cut" in results


def test_round_recommendations():
    recommender = HairstyleRecommender()

    results = recommender.get_recommendations("round")

    assert len(results) > 0


def test_unknown_shape():
    recommender = HairstyleRecommender()

    results = recommender.get_recommendations("unknown")

    assert len(results) == 1


def test_all_shapes():
    recommender = HairstyleRecommender()

    shapes = recommender.get_all_shapes()

    assert "oval" in shapes
    assert "round" in shapes
    assert "square" in shapes
    assert "heart" in shapes
    assert "diamond" in shapes
