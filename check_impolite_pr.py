from flask import Flask
from flask_restful import reqparse, Api, Resource
from ast import literal_eval
import requests

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('number')
parser.add_argument('action')
parser.add_argument('pull_request')

SUB_STRING = ['please', 'Please', 'PLEASE', 'appreciate', 'Appreciate', 'APPRECIATE'
              'would be great', 'Would Be Great', 'WOULD BE GREAT']
OWNER = "nik-git"
REPO = "king_impolite_pr_check"
TOKEN = "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"


class ImpolitePR(Resource):
    """
    Class to define REST API call to delete impolite PR.
    """
    def post(self):
        """
        POST method to delete impolite PR.
        Returns:

        """
        args = parser.parse_args()
        number = args['number']  # Get PR number
        pull_request = literal_eval(args.get("pull_request"))
        title = pull_request["title"]  # Get PR title
        body = pull_request["body"]  # Get PR body
        action = args["action"]  # Get PR action
        if action == 'opened':
            # Check if any of polite word in present in body of PR.
            # If not then close the PR.
            if not any(list(map(lambda x: True if x in body else False, SUB_STRING))):
                pr_url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{number}"
                params = {"title": f"{title}: Error - Impolite PR",
                          "state": "closed"}
                headers = {'Authorization': f'token {TOKEN}', "Accept": "application/vnd.github.v3+json"}
                response = requests.patch(pr_url, headers=headers, json=params)
                return response.json()
            else:
                return {"response": "This is a Polite PR."}
        else:
            return {"response": f"{action}: action on PR."}


api.add_resource(ImpolitePR, '/impolite_pr')


if __name__ == '__main__':
    app.run(debug=False)
