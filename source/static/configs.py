images_config = {
    "elements": [
        {
            "id": "start_string",
            "type": "string",
            "value": "startid"
        },
        {
            "id": "delimiter",
            "type": "string",
            "value": ";"
        },
        {
            "elements": [
                {
                    "id": "ID",
                    "type": "uint8"
                },
                {
                    "id": "delimiter",
                    "type": "string",
                    "value": ";"
                }
            ],
            "id": "Images",
            "type": "records"
        },
        {
            "id": "end_string",
            "type": "string",
            "value": "stopid"
        },
        {
            "id": "start_string",
            "type": "string",
            "value": "cns"
        },
        {
            "id": "delimiter",
            "type": "string",
            "value": ";"
        },
        {
            "format": {
                "alignment": "left",
                "fill": "\u0000"
            },
            "id": "StringOut0",
            "type": "blob"
        },
        {
            "id": "delimiter",
            "type": "string",
            "value": ";"
        },
        {
            "id": "end_string",
            "type": "string",
            "value": "cne"
        },
        {
            "elements": [
                {
                    "id": "jpeg_image",
                    "type": "blob"
                },
                {
                    "id": "raw_image",
                    "type": "blob"
                }
            ],
            "id": "Images",
            "type": "records"
        }
    ],
    "format": {
        "dataencoding": "ascii"
    },
    "layouter": "flexible"
}