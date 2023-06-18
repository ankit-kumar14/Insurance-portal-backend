# Insurance Premium Calculation API

This project provides an API for calculating insurance premiums based on user inputs such as age, sum insured, city tier, and tenure.

## Installation

1. Clone the repository:  
     `git clone https://github.com/your-username/insurance-premium-api.git`

2. Install the required dependencies: pip install -r `Flask` `pymongo` `python-dotenv`
3. Add this dataSet into your collection : https://drive.google.com/file/d/19L0oQ7TG2yor0MpirOfUmUBi5-e128V1/view

## Usage

1. Start the API server: `python main.py`

2. Make a POST request to the `/calculate_premium` endpoint with the required inputs in JSON format:

    POST `http://127.0.0.1:5000/calculate_premium`

    Request Body:
    {
    "ages": [35, 46, 10],
    "sum_insured": "500000",
    "city_tier": "1",
    "tenure": "1"
    }
    
    
    - `ages`: List of ages of insured members.
    - `sum_insured`: The sum insured for the policy.
    - `city_tier`: The city tier of residence.
    - `tenure`: The tenure of the insurance policy.
    
    Example Response: 
    `{
    "premium": 22933.0
    }`
    
    
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.




