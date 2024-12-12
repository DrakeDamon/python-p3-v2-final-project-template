# Athlete Performance Tracker

## Description

A command-line application that helps track athlete performance metrics and progress over time. Users can manage athletes, record performance test results, and analyze progress across various athletic metrics.

## Features

- Athlete Management (add, view, update, delete athletes)
- Performance Testing
  - Record test results (40-yard dash, vertical jump, agility, etc.)
  - View athlete's performance history
- Analysis Tools
  - Track progress over time
  - Find top performers in each category

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pipenv install
pipenv shell

Run the application:

bashCopypython lib/cli.py
Usage
Managing Athletes

Add new athletes with their basic information
View all registered athletes
Update athlete information
Remove athletes from the system

Recording Performances
Record various athletic metrics:

40-yard dash time
Vertical jump height
5-10-5 agility drill time
Flexibility score
Strength score
Additional notes

Analyzing Progress

Compare athlete's first and most recent performances
Track improvements in all measured metrics
Identify top performers in each category

Database Structure

Athletes Table: Stores athlete information
Performances Table: Stores test results with timestamps

Technologies Used

Python
SQLite3
Object-Relational Mapping (ORM)
```
