# Wappo game in Reinforcement Learning application

Rules of the game:

- Player (blue rhombus): takes one step per round
- Monster (red x): takes two steps per round; always takes the shortest route towards the player; always moves horizontally first, if no longer possible vertically
- Pentagram (orange star in cercle): monster is frozen for 3 rounds; to be frozen again, monster must re-enter the pentagram
- Goal (green house): player should reach house


![alt text](https://github.com/artem-istranin/wappo_game/blob/master/level_142_demo.png)

## Example

`python run_wappo_level.py 142`

https://user-images.githubusercontent.com/63958736/128630739-66657382-2c20-441f-a1dc-f892d7907f52.mp4

## References
- Rich Sutton and Andrew Barto. Reinforcement Learning: An Introduction, Second Edition, 2016.
