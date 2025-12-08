import sys

# --- Configuration ---
filename = "Day-01/Input.txt"
limit = 100         # The modulus (wrap-around point)
start_value = 50
# ---------------------
accumulator = start_value
zero_hits = 0

print(f"Reading from: {filename}")
print(f"Start Value: {accumulator}")

try:
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue

            opcode = line[0]
            operand = int(line[1:])
            
            # Execute OpCode
            if opcode == 'R':
                accumulator = (accumulator + operand) % limit
            elif opcode == 'L':
                accumulator = (accumulator - operand) % limit
            
            # --- Zero Detection Logic ---
            if accumulator == 0:
                zero_hits += 1
                # Optional: Mark the event in the log
                # print(f"Op: {line:<4} | Result: {accumulator} [ZERO DETECTED]")
            # ---------------------------------

    print(f"--- Simulation Complete ---")
    print(f"Final Value: {accumulator}")
    print(f"Times landed on zero: {zero_hits}")

except FileNotFoundError:
    print(f"Error: Could not find file at {filename}")