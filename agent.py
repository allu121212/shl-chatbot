from retriever import search_assessments


def needs_clarification(user_message):

    user_message = user_message.lower()

    vague_words = [
        "assessment",
        "test",
        "hiring"
    ]

    if len(user_message.split()) < 4:
        return True

    for word in vague_words:

        if word in user_message and len(user_message.split()) < 8:
            return True

    return False


def generate_response(messages):

    latest_message = messages[-1]["content"]

    if needs_clarification(latest_message):

        return {
            "reply": "What role are you hiring for and which skills should be assessed?",
            "recommendations": [],
            "end_of_conversation": False
        }

    full_query = " ".join([
        m["content"]
        for m in messages
    ])

    results = search_assessments(
        full_query,
        k=5
    )

    recommendations = []

    for item in results:

        recommendations.append({
     "name": item.get("name", "No Name"),
    "url": item.get("url", "No URL"),
    "test_type": "Assessment"
})
    return {
        "reply": "Here are recommended SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": True
    }