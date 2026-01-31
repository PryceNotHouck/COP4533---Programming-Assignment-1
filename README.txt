Pryce Houck (57790944)
Trevor DeBord (40228131)

Assumptions:
There will always be a new line in the input.txt file before the parameters
There will never be more than 1 new line in the output.txt file after the matchings

Usage Instructions:
Matcher - Place an input within the "input.txt" file in the same format as the included sample input,
          run the main branch at the bottom.

Verifier - Run Matcher with data within "input.txt". A corresponding matching list will be added to "output.txt",
            after running Matcher and populating the "output.txt" file, you can run verifier by executing the function at the bottom

Scalability - Can change the number of inputs by adjusting the size array in the main branch at the bottom

Sample inputs and outputs are included in the "input.txt" and "output.txt" files to begin with
There may be issues with file parsing if using VScode, Pycharm does not reproduce these errors

Dependencies & Assumptions:
Matcher.py and Verifier.py work with baseline Python 3.11 functionality, Scalability.py requires the environment
to include the matplotlib and numpy libraries, can be installed through pip or conda in terminal.

The graph produced by Scalability.py should automatically open a window displaying the result if it is being
run in an IDE, we do not know how this would change if it is being run through terminal.


Part C Approach and Observations:
{Images for graphs can be found in the parent directory in the repository}

Our approach to this problem, in Scalability.py, has two components: one to generate inputs, and one to
measure runtime.

The make_input(n: Integer) function takes a value n for the number of rows in either set of
preferences, generating an array of integers from 1 to n (inclusive). It then adds random shuffles of this
array to a set of preference table rows such that no two of the rows are the same. Finally, using these row arrays,
the values are populated into an output string in the desired format and returned.

In the main branch, an array of input sizes n is initialized in increasing powers of 2. For each n in sizes,
an input text is generated from make_input(n), and time.perf_counter() is invoked to record an initial timestamp.
A function from the matcher is then invoked to create tuple arrays for the recipient and proposer preference sets, which
are then passed into the Gale-Shapely algorithm (for the verifier, this output is then passed into the verifier).
The time.perf_counter() function is then invoked again to create a final timestamp, and the difference between the
two times are recorded as the runtime. Once all instances are recorded, matplotlib is used to create a scatterplot and
define a trendline over the datapoints, which is then formatted and displayed.

OBSERVATIONS:
You can observe that the runtime for the verifier is much lower. While the theoretical worst case for both is O(n^2) the
average runtime for the verifier is much lower because on average the hospitals will pick an applicant not very far down its
preference list, thus the inner loop will not have to search very deep because it can only be unstable if both sides have a higher
preference than their matching partners, so as soon as we reach its matched preference the inner loop terminates.
From preliminary testing it seems like the average runtime might actually be similar to O(logn) but not enough testing was done to confirm this
The matching algorithm appears to run in an expected O(n^2)