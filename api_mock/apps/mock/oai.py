# pylint: skip-file
specification = {
  "info": {
    "description": "Api mock usada para probar api-mgmt",
    "version": "1.0.0",
    "title": "Api-Mock"
  },
  "schemes": [
    "http"
  ],
  "paths": {
    "/echo": {
      "post": {
        "tags": [
          "misc"
        ],
        "summary": "Retorna todos los parametros y sus valores en formato json",
        "consumes": [
          "application/json"
        ],
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "successful operation"
          }
        }
      }
    },
    "/data.json": {
      "get": {
        "tags": [
          "data"
        ],
        "summary": "Retorna datos en formato json",
        "description": "",
        "consumes": [
          "application/json"
        ],
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Data"
            }
          }
        }
      }
    },
    "/data.csv": {
      "get": {
        "tags": [
          "data"
        ],
        "summary": "Retorna datos en formato csv",
        "description": "",
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/DataCSV"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Data": {
      "type": "object",
      "example": {
        "total": 2,
        "data": [
          {
            "id": 1,
            "username": "jhon"
          },
          {
            "id": 2,
            "username": "doe"
          }
        ]
      },
      "properties": {
        "total": {
          "type": "integer"
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "username": {
                "type": "string"
              }
            }
          }
        }
      }
    },
    "DataCSV": {
      "type": "string",
      "example": "id, username\n 1, john\n 2, doe"
    }
  }
}
