def progress_reward(progress, steps):
    if steps > 1:
        reward = progress / steps
    else:
        reward = 1
    return reward

print(progress_reward(0,2))