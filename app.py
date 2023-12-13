def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AIgit
    import vertexai

    # TODO(developer): Update and un-comment below lines
    # project_id = "PROJECT_ID"
    # location = "us-central1"

    vertexai.init(project=project_id, location=location)
    from vertexai.preview.generative_models import GenerativeModel, Part
    multimodal_model = GenerativeModel("gemini-pro-vision")
    response = multimodal_model.generate_content(
        [
            "what is shown in this image?",
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
        ]
    )
    print(response)
    return response.text