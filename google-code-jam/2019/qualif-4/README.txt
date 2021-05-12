"i.py" est une version élaguée de "interactive_runner.py" de Google.
Sa différence réside dans sa non interception du stderr afin d'aider à la mise au point.

"testing_tool.py" est le judge de Google, dont la couverture à améliorer => getTestCases()

Pour la mise au point :
python i.py python testing_tool.py 0 -- python q4.py


Pour les tests :
python interactive_runner.py python testing_tool.py 0 -- python q4.py