testall: tests # running the game and then pushing changes (if any) to git
	git add -A
	git commit -a -m "safe"
	git push

# running the game
tests: main.py game.py draw_shapes.py shapes.py game_manager.py particle.py physics_simulations.py
	/opt/homebrew/bin/python3 main.py