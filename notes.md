# Notes

## Prompt

Text that we give the LLM

## PromptTemplate

A wrapper class around a prompt

## Chat models

Wrappers around LLMs to allow us to interact with them as we would in a chat context.

## Chains

Allow us to combine several components into a singular application.

## Output Parser

An object that helps us parse the output of an LLM

## Agents

Agents perform actions on your behalf and interact with the LLM. Can use chain of thought prompting to allow the LLM to reason about what actions it needs to take to fulfill your requeast

https://arxiv.org/pdf/2201.11903v1

The LLMs ability to calculate these sub-tasks and organize its behavior is called ReAct

https://arxiv.org/pdf/2210.03629

### Tools

Agents use tools to connect to third-party services and actions
