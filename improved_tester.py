import numpy as np
import matplotlib.pyplot as plt
import time

class TypingTest:
    # initialise the typing test object:
    def __init__(self, words_file, words_per_round=8):
        self.words_list = self.read_CSV(words_file)
        self.words_per_round = words_per_round

    def read_CSV(self, csv_file):
        words_list = []
        with open(csv_file, 'r') as file:  # opens the file in read mode
            for line in file:
                # Split the line by comma to get individual words
                words = line.strip().split(',')
                # Extend the words list with the words from this line
                words_list.extend(words)
        return words_list

    def generate_random_words(self):
        random_indices = np.random.choice(len(self.words_list), self.words_per_round, replace=False)
        random_words = [self.words_list[i] for i in random_indices]
        return random_words
    
    def plot_results(self, round_times, round_accuracies):
        rounds = np.arange(1, len(round_times) + 1)

        plt.figure(figsize=(10, 5))

        # Plot-1: accuracy
        plt.subplot(1, 2, 1)
        plt.bar(rounds, round_accuracies,width=0.5, color='b', alpha=0.7) # plotting a bar chart for accuracy vs rounds
        plt.xlabel('Round')
        plt.ylabel('Accuracy (%)')
        plt.title('Typing Test Accuracy')

        # Plot-2: time
        plt.subplot(1, 2, 2)
        plt.plot(rounds, round_times, color='r',linestyle='--',marker='o') # plotting a line chart for time vs rounds
        plt.xlabel('Round')
        plt.ylabel('Time (seconds)')
        plt.title('Typing Test Time')

        plt.tight_layout()
        plt.show()


    def typing_test(self):
        print("Welcome to the Typing Test!")
        print("You have 1 minute to type as many words as possible.")
        print("Press Enter to start...")
        input()

        start_time = time.time()  # starts time count according to system clock
        end_time = start_time + 30  # setting the limit of 1 minute

        total_words_typed = 0
        total_correct_words = 0

        round_accuracies = []  # Store accuracy for each round
        round_time = []  # Store time for each round

        print("Type the following words:")
        while time.time() < end_time:  # loop to check the time limit

            if time.time() >= end_time:  # check time limit at the beginning of each round
                break

            round_words = self.generate_random_words()  # generates new set of words each round
            print()
            for word in round_words:
                print(word, end=' ')
            print("\n")

            typed_input = input()  # takes user's input
            typed_words = typed_input.split(' ')  # Split the user input into words
            total_words_typed += len(typed_words)  # increment the total words typed as the user types the words

            correct_words = '\0'
            correct_words = [word for word in typed_words if word in round_words]
            total_correct_words += len(correct_words)
            correct_words_arr = np.array([i for i in range(1,len(correct_words)+1)])

            # Calculate accuracy for the current round
            round_accuracy = (len(correct_words_arr)/self.words_per_round) * 100
            round_accuracies.append(round_accuracy)
            
            # Calculate time taken for the current round
            round_time.append(time.time() - start_time)

        time_taken = time.time() - start_time
        if total_words_typed > 0:
            accuracy = (total_correct_words / total_words_typed) * 100
        else:
            accuracy = 0
        wpm = (total_words_typed / time_taken) * 60  # calculate typing speed

        print("\nTest complete!")
        print(f"Total Words Typed: {total_words_typed}")
        print(f"Correct Words: {total_correct_words}")
        print("Accuracy: {:.2f}%".format(accuracy))
        print("Words Per Minute (WPM): {:.2f}".format(wpm))

        # Plotting the results
        self.plot_results(round_time, round_accuracies)

def main():
    words_file = "english_words.csv"
    typing_test = TypingTest(words_file)  # create typing test object of the class Typing test
    typing_test.typing_test()

if __name__ == "__main__": 
    main()
