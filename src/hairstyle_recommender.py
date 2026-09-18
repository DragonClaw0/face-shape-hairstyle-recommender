class HairstyleRecommender:
    """Provides hairstyle recommendations based on face shape."""

    def __init__(self):
        self.hairstyles = {
            "oval": [
                "Layered Cut",
                "Bob Cut",
                "Slick Back",
                "Side Part"
            ],

            "round": [
                "Pompadour",
                "Undercut",
                "High Volume Top",
                "Side Bangs"
            ],

            "square": [
                "Soft Waves",
                "Side Swept",
                "Textured Crop",
                "Fringe"
            ],

            "heart": [
                "Long Layers",
                "Pixie Cut",
                "Side Fringe",
                "Chin-length Bob"
            ],

            "diamond": [
                "Messy Fringe",
                "Shaggy Cut",
                "Shoulder Waves"
            ]
        }

    def get_recommendations(self, face_shape):
        """
        Return hairstyle recommendations for a face shape.

        Args:
            face_shape (str): Detected face shape.

        Returns:
            list: Recommended hairstyles.
        """

        face_shape = face_shape.lower().strip()

        return self.hairstyles.get(
            face_shape,
            ["No hairstyle recommendations available."]
        )

    def get_all_shapes(self):
        """Return all supported face shapes."""
        return list(self.hairstyles.keys())

    def add_hairstyle(self, face_shape, hairstyle):
        """
        Add a new hairstyle recommendation.

        Args:
            face_shape (str): Face shape.
            hairstyle (str): Hairstyle name.
        """

        face_shape = face_shape.lower().strip()

        if face_shape not in self.hairstyles:
            self.hairstyles[face_shape] = []

        if hairstyle not in self.hairstyles[face_shape]:
            self.hairstyles[face_shape].append(hairstyle)
