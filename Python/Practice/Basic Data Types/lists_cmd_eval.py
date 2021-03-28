#!/usr/bin/env python3

if __name__ == '__main__':
    lists = []
    for _ in range(int(input())):
        instruction = input().split()
        cmd = instruction[0]
        cmd_args = instruction[1:]
        if cmd == 'print':
            print(list(lists))
        else:
            cmd += "(" + ",".join(cmd_args) + ")"
            eval("lists.", cmd)
