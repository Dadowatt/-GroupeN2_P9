utils={
    "moussa_utils": {
        "version": "1.0",
        "description": "Utility functions for Moussa application",
        "functions": [
            {
                "name": "fetch_moussa_data",
                "description": "Fetch data for a specific Moussa item",
                "parameters": [
                    {
                        "name": "id",
                        "type": "integer",
                        "required": True,
                        "description": "ID of the Moussa item"
                    }
                ],
                "returns": {
                    "type": "json",
                    "description": "Moussa item data"
                },
                "errors": [
                    {
                        "code": 404,
                        "description": "Item not found"
                    }
                ]
            }
        ]

    }
    }

    