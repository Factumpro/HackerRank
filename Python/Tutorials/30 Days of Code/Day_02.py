#!/usr/bin/env python3


def solve(meal_cost,
          tip_percent, tax_percent):
    total_cost = (meal_cost
                  + ((meal_cost/100)*tip_percent)
                  + ((tax_percent/100)*meal_cost))
    return print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost,
          tip_percent, tax_percent)
