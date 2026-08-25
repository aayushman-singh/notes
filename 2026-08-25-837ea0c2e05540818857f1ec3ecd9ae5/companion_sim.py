def process(events):
    for e in events:
        if e['type']=='player_hit':
            yield f"[{e['msg']}] -> respond: Need healing?"
        elif e['type']=='enemy_spotted':
            yield f"[{e['msg']}] -> respond: Careful, enemy!"
        elif e['type']=='quest_update':
            yield f"[{e['msg']}] -> respond: Follow quest marker."
