import sys
import requests
from cto_ai import ux, sdk, prompt
import logo

def getAnswers():
  answers = []

  answers.append(prompt.input(
    name = "resp",
    message = "🙂 How do you feel today?"
    ))

  answers.append(prompt.input(
    name = "resp",
    message = "💻 What did you do since yesterday?"
    ))

  answers.append(prompt.input(
    name = "resp",
    message = "🚀 What will you do today?"
    ))

  answers.append(prompt.input(
    name = "resp",
    message = "🙅🚫 Anything blocking your progress?"
    ))
  return answers

def pingMembers():
  people = prompt.input(
    name = "resp",
    message = "👨👩 Which team members do you want a report from? (space separated list)"
    ).split()

  for _, value in enumerate(people):
    ux.print(f"@{value}")

  ux.print("📋 It's time for Standup! Use `/ops run nerdbot` to submit a report.")

def main():
  ux.print("Hello there! 👋 Time for your daily standup. \nPlease share what you've been working on.\n")
  answers = getAnswers()
  ux.print("")
  ux.print(f"🙂 How do you feel today? \n {answers[0]}")
  ux.print(f"💻 What did you do since yesterday? \n {answers[1]}")
  ux.print(f"🚀 What will you do today? \n {answers[2]}")
  ux.print(f"🙅🚫 Anything blocking your progress? \n {answers[3]}")

if __name__ == "__main__":
  logo.logo_print()
  ux.print("👋 Welcome to the CTO.ai NerdBot 👋")
  ux.print("This Op will allow you to manage your team's daily standups.\n")

  #  uncomment below for different functionality
  #  pingMembers() # uncomment and publish for team leads to ping team members
  main() # uncomment and publish for team members to submit reports
