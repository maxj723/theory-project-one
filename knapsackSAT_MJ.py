import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
from scipy.optimize import curve_fit

# solve knapsack problem similar to the dumb SAT 
def kp_SAT(value, coins):
    def dfs(curr, i, combo):
        if curr == value:
            return combo
        if i >= len(coins) or curr > value:
            return None
        skip = dfs(curr, i+1, combo)
        take = dfs(curr + coins[i], i+1, combo + [coins[i]])
        return skip if skip else take
    
    return dfs(0, 0, [])

# Read the test files and convert to usable format
def read_testfile(filename):
    tests = []
    with open(filename, 'r') as fp:
        for line in fp:
            test = line.strip().split(', ')
            test_dict = {'type': test[0],
                         'value': int(test[1]),
                         'coins': [int(c) for c in test[2:]]
            }
            tests.append(test_dict)
    return tests

# Run kp_SAT on test files
def run_tests(test_file, data_file):
    tests = read_testfile(f'Test_Files/{test_file}')
    file_exists = os.path.isfile(data_file)
    with open(data_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Number of Inputs', 'Execution Time', 'Is Satisfiable'])

        for test in tqdm(tests):
            # time each test
            start_time = time.time()
            solution = kp_SAT(test['value'], test['coins'])
            end_time = time.time()
            
            execution_time = end_time - start_time
            test_n = len(test['coins'])
            is_satisfiable = solution is not None

            # write to csv
            writer.writerow([test_n, execution_time, is_satisfiable])

# Plot all Results!
def plot_results(data_file):

    x_values = []
    y_values = []
    satis_x_values = []
    satis_y_values = []
    
    # Read values from CSV for plotting and analysis
    with open(data_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            n, time, is_satisfiable = int(row[0]), float(row[1]), row[2] == 'True'
            if is_satisfiable:
                satis_x_values.append(n)
                satis_y_values.append(time)
            else:
                x_values.append(n)
                y_values.append(time)

    # plot all times
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, marker='x', alpha=0.6, color='r', label='Unsatisfiable')
    plt.scatter(satis_x_values, satis_y_values, marker='.', alpha=0.6, color='b', label='Satisfiable')

    # Generate line of best fit for top 99.9% of values
    all_x = x_values + satis_x_values
    all_y = y_values + satis_y_values
    grouped_data = {}
    for x, y in zip(all_x, all_y):
        if x not in grouped_data:
            grouped_data[x] = []
        grouped_data[x].append(y)
    percentile_x = []
    percentile_y = []
    for x, y_values in grouped_data.items():
        percentile_x.append(x)
        percentile_y.append(np.percentile(y_values, 99.9))
    percentile_points = sorted(zip(percentile_x, percentile_y))
    percentile_x, percentile_y = zip(*percentile_points)

    def func(x, y):
        return y * 2**x
    params, _ = curve_fit(func, percentile_x, percentile_y)
    temp_fit = params[0]
    
    # Get line equation
    temp_fit_scientific = "{:.2e}".format(temp_fit)
    equation = f"y = {temp_fit_scientific} * 2^x"
    
    # Plot the worst case line
    x_range = np.linspace(min(percentile_x), max(percentile_x), 100)
    y_fit = func(x_range, temp_fit)
    plt.plot(x_range, y_fit, 'k--', label=f'Worst Case Fit: {equation}')

    # Finish plot
    plt.legend()
    plt.xlabel('# Inputs')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Knapsack Problem: Inputs vs Execution Time')
    plt.show()

def __main__():
    # iterate through all test files of different input values then plot
    for i in range(1, 23):
        filename = f'test{i}.txt'
        run_tests(filename, 'data_times_max.csv')
    plot_results('data_times_max.csv')
    


if __name__ == '__main__':
    __main__()