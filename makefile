testall: tests # running the game and then pushing changes (if any) to git
	git add -A
	git commit -a -m "safe"
	git push

# running the game
tests: src/main.py src/game.py src/draw_shapes.py src/shapes.py src/game_manager.py src/particle.py src/physics_simulations.py
	/opt/homebrew/bin/python3 src/main.py