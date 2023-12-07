# # import random
# # class Sentences:

# #     def __init__(self, determiner, singular_nouns, plural_nouns, past_verbs, present_verbs, future_verbs):
# #         self.determiner = ["a", "one", "the", "some", "many"]
# #         self.singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
# #         self.plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
# #         self.past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
# #         self.present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
# #         self.future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

# #    # sample method 1
# #     def get_determiner(self, quantity):
# #         """Return a randomly chosen determiner. A determiner is
# #         a word like "the", "a", "one", "some", "many".
# #         If quantity is 1, this function will return either "a",
# #         "one", or "the". Otherwise this function will return
# #         either "some", "many", or "the".

# #         Parameter
# #             quantity: an integer.
# #                 If quantity is 1, this function will return a
# #                 determiner for a single noun. Otherwise this
# #                 function will return a determiner for a plural
# #                 noun.
# #         Return: a randomly chosen determiner.
# #         """
# #         if quantity == 1:
# #             words = ["a", "one", "the"]
# #         else:
# #             words = ["some", "many", "the"]

# #         # Randomly choose and return a determiner.
# #         word = random.choice(words)
# #         return word

# #         # sample method 1
# #     def get_noun(self, quantity):
# #         """Return a randomly chosen noun.
# #         If quantity is 1, this function will
# #         return one of these ten single nouns:
# #             "bird", "boy", "car", "cat", "child",
# #             "dog", "girl", "man", "rabbit", "woman"
# #         Otherwise, this function will return one of
# #         these ten plural nouns:
# #             "birds", "boys", "cars", "cats", "children",
# #             "dogs", "girls", "men", "rabbits", "women"

# #         Parameter
# #             quantity: an integer that determines if
# #                 the returned noun is single or plural.
# #         Return: a randomly chosen noun.
# #         """
# #         if quantity == 1:
# #             return random.choice(self.singular_nouns)
# #         else:
# #             return random.choice(self.plural_nouns)


# #      # sample method 1
# #     def get_verb(self, quantity, tense, verbs):
# #         """Return a randomly chosen verb. If tense is "past",
# #         this function will return one of these ten verbs:
# #             "drank", "ate", "grew", "laughed", "thought",
# #             "ran", "slept", "talked", "walked", "wrote"
# #         If tense is "present" and quantity is 1, this
# #         function will return one of these ten verbs:
# #             "drinks", "eats", "grows", "laughs", "thinks",
# #             "runs", "sleeps", "talks", "walks", "writes"
# #         If tense is "present" and quantity is NOT 1,
# #         this function will return one of these ten verbs:
# #             "drink", "eat", "grow", "laugh", "think",
# #             "run", "sleep", "talk", "walk", "write"
# #         If tense is "future", this function will return one of
# #         these ten verbs:
# #             "will drink", "will eat", "will grow", "will laugh",
# #             "will think", "will run", "will sleep", "will talk",
# #             "will walk", "will write"

# #         Parameters
# #             quantity: an integer that determines if the
# #                 returned verb is single or plural.
# #             tense: a string that determines the verb conjugation,
# #                 either "past", "present" or "future".
# #         Return: a randomly chosen verb.
# #         """

# #         if tense == "past":
# #             return random.choice(self.past_verbs)
# #         elif tense == "present":

# #                 if quantity == 1:
# #                     return random.choice(self.present_verbs)
# #                 else:
# #                     return random.choice(self.present_verbs).rstrip('s')
# #         elif tense == "future":
# #             return random.choice(self.future_verbs)
# #         else:
# #             return "Invalid tense"


# #       # sample method 1
# #     def make_sentence(self, quantity, tense):
# #         """Build and return a sentence with three words:
# #         a determiner, a noun, and a verb. The grammatical
# #         quantity of the determiner and noun will match the
# #         number in the quantity parameter. The grammatical
# #         quantity and tense of the verb will match the number
# #         and tense in the quantity and tense parameters.
# #         """

# #         determiner = self.get_determiner(quantity)
# #         noun = self.get_noun(quantity)
# #         verb = self.get_verb(quantity, tense)
# #         sentence = f"{determiner.capitalize()} {noun} {verb}."
# #         return sentence


# # def main():
# #       # Define a list of combinations of quantity and tense.
# #     combinations = [
# #         ("single", "past"),
# #         ("single", "present"),
# #         ("single", "future"),
# #         ("plural", "past"),
# #         ("plural", "present"),
# #         ("plural", "future"),
# #     ]

# #     #Create a Sentence

# #     sentence = Sentences(
# #     determiner=["a", "one", "the", "some", "many"],
# #     singular_nouns=["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"],
# #     plural_nouns=["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"],
# #     past_verbs=["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
# #     present_verbs=["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
# #     future_verbs=["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
# # )


# #      # Iterate through the combinations and generate and print sentences.
# #     for quantity, tense in combinations:
# #         sentence = sentence.make_sentence(quantity, tense)
# #     print(f"{quantity.capitalize()} {tense.capitalize()}: {sentence}")


# # if __name__ == '__main__':
# #     main()

# import random

# class Sentences:

#     def __init__(self):
#         self.determiner = ["a", "one", "the", "some", "many"]
#         self.singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
#         self.plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
#         self.past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
#         self.present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
#         self.future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

#     def get_determiner(self, quantity):
#         if quantity == "single":
#             return random.choice(["a", "one", "the"])
#         else:
#             return random.choice(["some", "many", "the"])

#     def get_noun(self, quantity):
#         if quantity == "single":
#             return random.choice(self.singular_nouns)
#         else:
#             return random.choice(self.plural_nouns)

#     def get_verb(self, quantity, tense):
#         if tense == "past":
#             return random.choice(self.past_verbs)
#         elif tense == "present":
#             if quantity == "single":
#                 return random.choice(self.present_verbs)
#             else:
#                 return random.choice(self.present_verbs).rstrip('s')
#         elif tense == "future":
#             return random.choice(self.future_verbs)
#         else:
#             return "Invalid tense"

#     def make_sentence(self, quantity, tense):
#         determiner = self.get_determiner(quantity)
#         noun = self.get_noun(quantity)
#         verb = self.get_verb(quantity, tense)
#         sentence = f"{determiner.capitalize()} {noun} {verb}."
#         return sentence

# def main():
#     # Define a list of combinations of quantity and tense.
#     combinations = [
#         ("single", "past"),
#         ("single", "present"),
#         ("single", "future"),
#         ("plural", "past"),
#         ("plural", "present"),
#         ("plural", "future"),
#     ]

#     # Create a Sentence
#     sentence_generator = Sentences()

#     # Iterate through the combinations and generate and print sentences.
#     for quantity, tense in combinations:
#         sentence = sentence_generator.make_sentence(quantity, tense)
#         print(f"{quantity.capitalize()} {tense.capitalize()}: {sentence}")

# if __name__ == '__main__':
#     main()

print

import random


class Sentence:
    def __init__(self):
        self.determiners = ["a", "one", "the", "some", "many"]
        self.singular_nouns = [
            "bird",
            "boy",
            "car",
            "cat",
            "child",
            "dog",
            "girl",
            "man",
            "rabbit",
            "woman",
        ]
        self.plural_nouns = [
            "birds",
            "boys",
            "cars",
            "cats",
            "children",
            "dogs",
            "girls",
            "men",
            "rabbits",
            "women",
        ]
        self.past_verbs = [
            "drank",
            "ate",
            "grew",
            "laughed",
            "thought",
            "ran",
            "slept",
            "talked",
            "walked",
            "wrote",
        ]
        self.present_verbs = [
            "drinks",
            "eats",
            "grows",
            "laughs",
            "thinks",
            "runs",
            "sleeps",
            "talks",
            "walks",
            "writes",
        ]
        self.future_verbs = [
            "will drink",
            "will eat",
            "will grow",
            "will laugh",
            "will think",
            "will run",
            "will sleep",
            "will talk",
            "will walk",
            "will write",
        ]
        self.prepositions = [
            "about",
            "above",
            "across",
            "after",
            "along",
            "around",
            "at",
            "before",
            "behind",
            "below",
            "beyond",
            "by",
            "despite",
            "except",
            "for",
            "from",
            "in",
            "into",
            "near",
            "of",
            "off",
            "on",
            "onto",
            "out",
            "over",
            "past",
            "to",
            "under",
            "with",
            "without",
        ]
        self.adjectives = [
            "happy",
            "beautiful",
            "clever",
            "colorful",
            "delicious",
            "energetic",
            "friendly",
            "gentle",
            "mysterious",
            "peaceful",
        ]
        self.adverbs = [
            "quickly",
            "softly",
            "loudly",
            "carefully",
            "suddenly",
            "easily",
            "patiently",
            "slowly",
            "gracefully",
            "happily",
        ]

    def get_determiner(self, quantity):
        """Return a randomly chosen determiner. A determiner is
        a word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either "a",
        "one", or "the". Otherwise this function will return
        either "some", "many", or "the".

        Parameter
            quantity: an integer.
                If quantity is 1, this function will return a
                determiner for a single noun. Otherwise this
                function will return a determiner for a plural
                noun.
        Return: a randomly chosen determiner.
        """
        if quantity == "single":
            return random.choice(self.determiners)
        else:
            return random.choice(self.determiners)

    def get_noun(self, quantity):
        """Return a randomly chosen noun.
        If quantity is 1, this function will
        return one of these ten single nouns:
            "bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"
        Otherwise, this function will return one of
        these ten plural nouns:
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"

        Parameter
            quantity: an integer that determines if
                the returned noun is single or plural.
        Return: a randomly chosen noun.
        """

        return random.choice(self.singular_nouns)

    def get_verb(self, quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.

            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """
        if tense == "past":
            return random.choice(self.past_verbs)
        elif tense == "present":
            if quantity == "single":
                return random.choice(self.present_verbs)
            else:
                return random.choice(self.present_verbs).rstrip("s")
        elif tense == "future":
            return random.choice(self.future_verbs)

    def get_adjective(self):
        """Return a randomly chosen adjective from a list of adjectives."""
        return random.choice(self.adjectives)

    def get_adverb(self):
        """Return a randomly chosen adverb from a list of adverbs."""
        return random.choice(self.adverbs)

    def get_preposition(self):
        """Return a randomly chosen preposition
        from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

        Return: a randomly chosen preposition.
        """

        return random.choice(self.prepositions)

    def get_prepositional_phrase(self, quantity):
        """Build and return a prepositional phrase composed
        of three words: a preposition, a determiner, and a
        noun by calling the get_preposition, get_determiner,
        and get_noun functions.

        Parameter
            quantity: an integer that determines if the
                determiner and noun in the prepositional
                phrase returned from this function should
                be single or plural.
        Return: a prepositional phrase.
        """
        determiner = self.get_determiner(quantity)
        adjective = self.get_adjective()
        preposition = self.get_preposition()
        noun = self.get_noun(quantity)
        return f"{determiner} {adjective} {noun} {preposition}"

    def make_sentence(self, quantity, tense):
        """Build and return a sentence with four parts:
        a determiner, a noun, a verb, and a prepositional phrase.
        The grammatical quantity of the determiner and noun will
        match the number in the quantity parameter. The grammatical
        quantity and tense of the verb will match the number and
        tense in the quantity and tense parameters.

        Parameter
            quantity: an integer that determines if the determiner
                and noun should be single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
            verb: a string representing the verb.
        """
        determiner = self.get_determiner(quantity)
        adjective = self.get_adjective()
        noun = self.get_noun(quantity)
        prepositional_phrase1 = self.get_prepositional_phrase(quantity)
        adverb = self.get_adverb()
        verb = self.get_verb(quantity, tense)
        prepositional_phrase2 = self.get_prepositional_phrase(quantity)

        # Rearranged order
        # return f"{determiner} {adjective} {noun} {prepositional_phrase1}"
        return f"{determiner} {adjective} {noun} {verb} {prepositional_phrase1}, {adjective} {noun} {adverb} {verb} {prepositional_phrase2}."


def main():
    sentence_generator = Sentence()

    quantities = ["single", "plural"]
    tenses = ["past", "present", "future"]

    for quantity in quantities:
        for tense in tenses:
            sentence = sentence_generator.make_sentence(quantity, tense)
            # Removing the unwanted words from the print statement
            print(f"{sentence.capitalize()}")


if __name__ == "__main__":
    main()
