from retriever import search_assessments

def chat_agent(messages):

    latest_message = messages[-1]["content"].lower()

    vague_words = [
        "assessment",
        "test",
        "hiring",
        "developer",
        "engineer"
    ]

   
    if len(latest_message.split()) <= 3:
        return {
            "reply": "Could you share more details about the role, seniority level, and required skills?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Off-topic r
    off_topic = [
        "weather",
        "movie",
        "cricket",
        "politics",
        "legal"
    ]

    for word in off_topic:
        if word in latest_message:
            return {
                "reply": "I can only help with SHL assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": True
            }

    # Comparison support
    if "difference" in latest_message or "compare" in latest_message:
        return {
            "reply": "OPQ measures personality and behavioral preferences, while GSA evaluates general cognitive and problem-solving ability.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Retrieve recommendations
    results = search_assessments(latest_message)

    recommendations = []

    for item in results[:5]:

        recommendations.append({
            "name": item.get("name", "Unknown"),
            "url": item.get("url", ""),
            "test_type": "Assessment"
        })

    return {
        "reply": f"Here are {len(recommendations)} SHL assessments matching your requirements.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }