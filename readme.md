To the grader:

This program is written in Python 2.7.
Packages networkx and matplotlib are required for graph tools and visual display.

As required, this program allows the user to interact with the working model to
select the function to be accomplished.  The program starts with a single node
and allows the user to add nodes, which will be added at a random point in the
ring.

The software should work for all cases:

1. Adding nodes
   - generates id
   - gets successor and predecessor
   - updates for successor and predecessor of new node's presence
   - repeats if new id conflicts with existing node
2. Deletion of nodes
   - takes node id from user
   - removes node
   - notifies successor and predecessor
3. Lookup of data (** my intention is to qualify for the 20 pt bonus **)
   - takes node id and lookup id from user
   - uses table entries as it progresses through Chord to locate the data id
   - returns information about hops along the path as well as the data once it is found
4. Node configuration information can be viewed
   - successor id
   - predecessor id
   - finger table info

Thank you,
David Rosenberg
U00063482
