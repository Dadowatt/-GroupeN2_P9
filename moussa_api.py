
api = {
    "name": "Moussa API",
    "version": "1.0",
    "description": "API for Moussa application",
    "endpoints": [
        {
            "path": "/moussa",
            "method": "GET",
            "description": "Fetch Moussa data",
            "parameters": [
                {
                    "name": "id",
                    "type": "integer",
                    "required": True,
                    "description": "ID of the Moussa item"
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content_type": "application/json"
                },
                "404": {
                    "description": "Item not found"
                }
            }
        }   
    ],
    "authentication": {
        "type": "Bearer Token",
        "description": "Use a valid bearer token to access the API"
    },
    "rate_limit": {
        "requests_per_minute": 60,
        "description": "Maximum number of requests allowed per minute"
    },  
}
