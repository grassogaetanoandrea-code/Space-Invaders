def check_collision(obj1, obj2):
    # Ritorna True se due oggetti sono nella stessa posizione
    return obj1.x == obj2.x and obj1.y == obj2.y

def handle_bullet_enemy_collision(bullets, enemies):
    # Controlla ogni proiettile contro ogni nemico
    for b in bullets:
        for e in enemies:
            if check_collision(b, e):
                bullets.remove(b)
                enemies.remove(e)
                return True
    return False