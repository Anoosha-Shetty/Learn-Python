#Wordcount program
text = """/n
        Lists and Tuples
    Python uses both lists and tuples. In general, tuples are used when the position of an element indicates something
    about its capability, and lists are used to hold elements that will be treated in the same manner. Python doesn't enforce
    these constraints, though; the only hard and fast rule for using lists and tuples is don't use tuples if you want to change
    the sequence. Tuples are primarily for use when you need a non-modifiable sequence.
    Writing Lists and Tuples
    Sometimes you'll want to write the contents of a list right inside of your code. To do that, write a comma-separated list
    of the element values, surrounded by square brackets [ ].
    Tuples are usually written as a comma-separated list of values surrounded by parentheses ( ) rather than brackets [ ],
    but in many cases the parentheses () are optional. (Okay, I will refrain from including illustrations of brackets [ ] and
    parentheses ( ) now. You get the picture, right?) The interactive interpreter always puts parentheses around a tuple
    when asked to display its representation, and we recommend you do the same, in order to facilitate readability.
    Let's look at some sequences in action. Start an interactive terminal session and type:
    INTERACTIVE SESSION:
    cold1:~$ python3
    >>> lst1 = [1, 3, 5]
    >>> lst2 = [2, 4, 6]
    >>> tup1 = (9, 7, 5)
    >>> tup2 = (8, 6, 4)
    >>> dir(lst1)
    ['__add__', '__class__', '__contains__', ... , 'append', 'count', 'extend',
    'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> dir(tup1)
    ['__add__', '__class__', '__contains__', ... , 'count', 'index']
    >>> lst1+lst2
    [1, 3, 5, 2, 4, 6]
    >>> tup1+tup2
    (9, 7, 5, 8, 6, 4)
    >>> lst1+tup1
    Traceback (most recent call last):
    File "<console>", line 1, in <module>
    TypeError: can only concatenate list (not "tuple") to list
    >>> clist = [lst1, lst2, tup1, tup2]
    >>> print(clist)
    [[1, 3, 5], [2, 4, 6], (9, 7, 5), (8, 6, 4)]
    The results of the calls to the dir() function show that a list has methods that a tuple doesn't have. We abbreviated the
    output by removing many of the special names beginning with a double underscore. We'll learn more about those
    methods later, but for now we'll focus on the regular methods.
    You can put whatever you like in a list. Usually you'll enter simple values like strings and numbers. The clist list in the
    example above contains two other lists and two tuples.
    Accessing Sequence Values
    Once you have created a sequence, you can access its individual elements using indexing. To index a single element
    from a sequence, you follow it with a numeric value in square brackets (remember—the first element is numbered
    zero!). You can also take slices from the sequence, creating a new and usually smaller sequence. To slice a sequence,
    you write two numeric values, separated by a colon (:), inside the square brackets. If you omit the first value, the new
    sequence starts with the first element of the sliced sequence. If you omit the last value, the new sequence ends with its
    last element. Continue the interactive terminal session as shown:
    INTERACTIVE SESSION:
    >>> clist = [1, (2, 3, 4), "a", "Bright", "c"]
    >>> clist [1]
    (2, 3, 4)
    >>> clist[1][1]
    3
    >>> clist[3][1:3]
    'ri'
    >>> stuff = clist[2:4]
    >>> stuff
    ['a', 'Bright']
    >>> stuff2 = clist[2:5]
    >>> stuff2
    ['a', 'Bright', 'c']
    >>> stuff[0]
    'a'
    >>> "Strings are sequences too"[:7]
    'Strings'
    Indexing and slicing are fundamental operations in Python, so make sure that you understand why each expression
    evaluates the way it does. Be aware that when you slice a sequence, the second index isn't the index of the last
    element in the slice. This is actually very useful. It would be confusing if clist [2:4] didn't give you a list 2 elements
    long, so element 4 isn't included in that slice. So, to get the fourth element in our slice, we referenced the nonexistent
    element 5. Because strings are also sequences, we can chop strings up without too much difficulty.
    Modifying Lists
    Although strings and tuples are also sequences, they are immutable. Once created, they can't be changed (although
    you can still index and slice them to extract individual elements or sub-sequences). Lists, however, can be changed. In
    the same way that you can bind a new value to a name with an assignment, you can also bind a new value to an
    element of a list. Let's check out one way you can modify a list. Start or continue the interactive terminal session as
    shown:
    INTERACTIVE SESSION:
    >>> stuff = [1, (2, 3, 4), "a", "Bright", "c"]
    >>> stuff[1] = "Not a tuple"
    >>> stuff
    [1, 'Not a tuple', 'a', 'Bright', 'c']
    >>> stuff[0] = 0
    >>> stuff[3] = 'b'
    >>> stuff
    [0, 'Not a tuple', 'a', 'b', 'c']
    >>> stuff[2:4]
    ['a', 'b']
    >>> stuff[2:4] = [1, 2, 3]
    >>> stuff
    [0, 'Not a tuple', 1, 2, 3, 'c']
    >>>
    So far, we've just been just replacing single elements of the list. It's also possible to replace a slice. When you do that,
    make sure that you also assign another sequence. Any sequence will do—a list, tuple, or string. If you assign a string
    to a slice, each character in the string becomes a new element of the list. Try experimenting with these possibilities.
    Because you can replace any slice of a list, you can delete the slice by assigning an empty sequence to it. But there are
    less labor-intensive ways to replace a slice of a list. Python's del statement was designed especially for deleting
    things. You can use it on a single element or a slice. If you know that a list contains a certain value, but you don't know
    the value's index, you can use the list's remove() method to delete it from the list. If the same value occurs more than
    once, only the first occurrence is deleted. Let's give it a try. Type the commands below as shown:
    INTERACTIVE SESSION:
    >>> dlist = ['a', 'b', 'c', '1', '2', 1, 2, 3]
    >>> dlist[6]
    2
    >>> del dlist[6]
    >>> dlist
    ['a', 'b', 'c', '1', '2', 1, 3]
    >>> dlist[:3]
    ['a', 'b', 'c']
    >>> del dlist[:3]
    >>> dlist
    ['1', '2', 1, 3]
    >>> dlist.remove(1)
    >>> dlist
    ['1', '2', 3]
    Note
    In the last example, element 2 (the integer 1) was removed, not element 0 (the string '1'). In Python,
    numbers and strings are distinctive, and it doesn't convert from one to the other unless you specifically
    tell it to do so.
    Also, remember that deletion only works for lists. Deleting an element of a sequence would be the same
    as modifying the sequence, and you can't modify tuples and strings.
    As we saw in an earlier example, we can add elements to a list. Another way to include more elements is to use the
    list's append() method. You call the method and give it a new element to be appended to the list. It's also possible to
    insert elements at a specific position, and again there are two ways to do this. The simplest way is to use the list's
    insert () method, which you call with a position (index value) and a value to be inserted. Or you could also assign the
    new value to an empty slice—any slice with the same value for the lower and upper indexes is bound to be empty.
    Let's experiment with adding new elements to a list. Type the commands below as shown:
    INTERACTIVE SESSION:
    >>> elist = [] # The empty list
    >>> elist.append('a')
    >>> elist
    ['a']
    >>> elist.append('b')
    >>> elist
    ['a', 'b']
    >>> elist.append((1, 2, 3))
    >>> elist
    ['a', 'b', (1, 2, 3)]
    >>> len(elist)
    3
    >>> elist[1:1]
    []
    >>> elist[1:1] = ["new second element"]
    >>> elist
    ['a', 'new second element', 'b', (1, 2, 3)]
    >>> elist.insert(3, "4th")
    >>> elist
    ['a', 'new second element', 'b', '4th', (1, 2, 3)]
    >>> len(elist)
    5
    One of the limitations we run into with slice assignment is that the replacement must be a sequence, so we usually
    append or insert it. If you have a sequence of elements that you want to insert, keep in mind that slice assignment
    requires much less code than most other techniques.
    Note
    If you call a list's append() method with a sequence argument (like you did with elist .append((1, 2, 3))
    in the example above), that entire sequence becomes the last element of the list.
    Slices with a Stride: Skipping Sequences
    A slice specifies a subsequence of a sequence. Now suppose you don't want to include every element, but instead
    you want to use every second or third element. The easiest way to do this would be to use a third component of the
    slice specification: the stride. The stride specifies how many elements to skip in the slice before extracting the next
    element. The stride is separated from the first two components with a colon; so your slice specification is like
    [first:last:stride].
    When you specify only two slice components, by default the stride is 1; it takes every element in the slice. A stride of 2
    takes every second element, and so on. Stride values can be negative as well as positive. Slicing always works by
    setting the index to the first slicing component and then increasing the index by the stride value, until the index reaches
    or goes past the second slicing component. When the stride is negative, the first slicing component must be higher
    than the second. Type the commands below as shown:
    INTERACTIVE SESSION:
    >>> alf = "abcdefghijklmnopqrstuvwxyz"
    >>> alf[2:13]
    'cdefghijklm'
    >>> alf[2:13:2]
    'cegikm'
    >>> alf[2:13:-2]
    ''
    >>> alf[13:2:-2]
    'nljhfd'
    >>> alf[13:2]
    ''
    >>> alf[::-1]
    'zyxwvutsrqponmlkjihgfedcba'
    One way to get the reverse of a sequence is to slice the whole thing by omitting the first and second slice components
    and then use a stride of -1. So, if you want to replace a list with its reverse, rather than use the list's reverse() method
    lst.reverse(), you can write lst = lst[::-1]. Python sequences are nothing if not versatile!
    Other Functions and Methods to Use with Sequences
    Sometimes you'll have a string that you want to break up into a list of words. The split () method helps you to do just
    that. If you call the string without any arguments, it will split the string. If you call it with one argument (for example, a
    space " "), it will use that argument as a separator, returning a list of the strings that appear between its occurrences.
    If you give a second argument, it should be an integer. This informs the interpreter of the maximum number of times to
    recognize the separator, which limits the number of elements in the returned list.
    To get the sum of the numbers in a sequence, pass the sequence to the sum() function as an argument. The
    interpreter will raise an exception if there is a non-numeric element in the sequence. To get the length of any sequence,
    use the len() function.
    To find the number of times a particular element appears in a list or tuple, use the count () method, with the element
    value you are seeking as the argument.
    Testing for Presence in a Sequence
    To determine whether a sequence contains a specific value, use the in keyword, which returns either True or False.
    Sequences also have an index() method that will return the lowest index value at which a given element occurs. You
    have to be careful using index() though, as it will raise an exception if the element isn't present. To avoid the
    exception, you can use an if test to ensure that the value is present, but it's better just to handle the exception, and
    avoid doing the search twice. We'll cover the if statement and exception handling in detail later.
    Manipulating Lists and Tuples
    Create a new program file as shown:
    CODE TO TYPE:
    #!/usr/local/bin/python3

    Simpler program to list the words of a string.
    s = input("Enter your string: ")
    words = s.strip().split()
    for word in words:
    print(word)
    Save it in your /pyt hon1 folder as bet t er_sent ence_split t er.py and run it. This code performs the same tasks as
    the one we wrote in the last lesson, but it uses features built into the Python language. Now type in a string that
    contains some white space, press Ent er, and examine the result. You should see the list of words, printed one per
    line.
    OBSERVE:
    s = input("Enter your string: ")
    words = s.strip().split()
    for word in words:
    print(word)
    This code applies the strip() method to string s, which returns a string with no leading or trailing white space. The
    split () method is then applied to the already stripped string, returning a list of the words. The f or loop iterates over the
    list, printing each word on a separate line.
    Now let's do something a little more complex with lists. We'll take a long piece of text and find out how many lines,
    words, and characters it contains. To determine the number of characters, use the len() method. We count the lines by
    splitting the text to get a list of them. Finally, we split each line into words and accumulate a total by adding the number
    of words in each line together.
    Create a new file in the editor window as shown:
    CODE TO TYPE:
    #!/usr/local/bin/python3

    Count the words, lines and characters in a chunk of text.
    gettysburg = 
    Four score and seven years ago our
    fathers brought forth on this continent,
    a new nation, conceived in Liberty, and
    dedicated to the proposition that
    all men are created equal.
    Now we are engaged in a great civil war,
    testing whether that nation, or
    any nation so conceived and so dedicated,
    can long endure. We are met on
    a great battle-field of that war. We have
    come to dedicate a portion of that
    field, as a final resting place for those
    who here gave their lives that that
    nation might live. It is altogether
    fitting and proper that we should do this.
    charct = len(gettysburg)
    lines = gettysburg.split("\n")
    linect = len(lines)
    wordct = 0
    for line in lines:
    words = line.split()
    wordct += len(words)
    print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.
    ")
    Save it in your /pyt hon1 folder as paragraph_st at s.py and run it. If you typed in exactly the same input text, you'll
    see The t ext cont ains 16 lines, 102 words, and 557 charact ers.
    Note
    Some operating systems may give different results; for example, Unix records a newline as one
    character, while Windows records it as two.
    Okay, now let's modify our program to keep a count of word lengths, so we know how many one-letter, two-letter, and
    three-letter words there are, and so on. Modify your paragraph_stats.py file as shown:
    CODE TO TYPE:
    #!/usr/local/bin/python3
    Count the words, lines and characters in a chunk of text.
    gettysburg = 
    Four score and seven years ago our
    fathers brought forth on this continent,
    a new nation, conceived in Liberty, and
    dedicated to the proposition that
    all men are created equal.
    Now we are engaged in a great civil war,
    testing whether that nation, or
    any nation so conceived and so dedicated,
    can long endure. We are met on
    a great battle-field of that war. We have
    come to dedicate a portion of that
    field, as a final resting place for those
    who here gave their lives that that
    nation might live. It is altogether
    fitting and proper that we should do this.
    lengthct = [0]*20 # a list of 20 zeroes
    charct = len(gettysburg)
    lines = gettysburg.split("\n")
    linect = len(lines)
    wordct = 0
    for line in lines:
    words = line.split()
    wordct += len(words)
    for word in words:
    lengthct[len(word)] += 1
    print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.
    ")
    for i, ct in enumerate(lengthct):
    if ct:
    print("Length", i, ":", ct)
    In the new program, we begin by creating a list of counts. The idea is that the count of n-letter words will be kept in
    lengt hct [n], and we assume that no word will be longer than 19 characters. Sometimes that kind of assumption can
    be dangerous, but for now, for experimentation's sake, we'll just go with it. In the loop that processes each line, we
    have added a loop to iterate over the words. The length of each word is used as an index into the lengt hct list, and
    that element is incremented by one (they all start at zero). Finally, when the text has been fully processed, there is a bit
    more code used to output the count of words of each length. The only real wrinkle here is the if statement that omits
    those lengths for which there aren't any words.
    Save and run it. Your output will look like this:
    So far, so good. Go on and experiment some more. Modify the text so it contains a word of twenty characters or more
    (like "deinstitutionalizing"). What happens when you run the program? How could you make the program work again? 
    Can you think of a way you might modify the program to keep a count of the individual words, so you could see how 
    many times each word was used? Using only sequences, this is pretty difficult, but not impossible."""



charlen = len(text)

lines = text.split("\n")
linect = len(lines)

words = text.split()
wrdct = len(words)

print("No of characters: ", charlen, """\n""", "No of lines: ", linect, """\n""" "No of words: ", wrdct)
