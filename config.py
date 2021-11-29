from switch import Switch
from cable import Cable
import gc


def main():
    switch_a = Switch("a", ["b", "c", "d"], {1: "down", 2: "down", 3: "down", 4: "down", 5: "down", 6: "down"})
    switch_b = Switch("b", ["c", "d", "a"], {1: "down", 2: "down", 3: "down", 4: "down", 5: "down", 6: "down"})
    switch_c = Switch("c", ["d", "a", "c"], {1: "down", 2: "down", 3: "down", 4: "down", 5: "down", 6: "down"})
    switch_d = Switch("d", ["a", "b", "c"], {1: "down", 2: "down", 3: "down", 4: "down", 5: "down", 6: "down"})

    switches = []

    a_to_b_1 = Cable()
    a_to_b_1_v = a_to_b_1.link("a", 1, "b", 1)
    switches.append(a_to_b_1_v)

    a_to_b_2 = Cable()
    a_to_b_2_v = a_to_b_2.link("a", 2, "b", 2)
    switches.append(a_to_b_2_v)

    a_to_c_1 = Cable()
    a_to_c_1_v = a_to_c_1.link("a", 3, "c", 1)
    switches.append(a_to_c_1_v)

    a_to_c_2 = Cable()
    a_to_c_2_v = a_to_c_2.link("a", 4, "c", 2)
    switches.append(a_to_c_2_v)

    a_to_d_1 = Cable()
    a_to_d_1_v = a_to_d_1.link("a", 5, "d", 1)
    switches.append(a_to_d_1_v)

    a_to_d_2 = Cable()
    a_to_d_2_v = a_to_d_2.link("a", 6, "d", 2)
    switches.append(a_to_d_2_v)

    b_to_c_1 = Cable()
    b_to_c_1_v = b_to_c_1.link("b", 3, "c", 3)
    switches.append(b_to_c_1_v)

    b_to_c_2 = Cable()
    b_to_c_2_v = b_to_c_2.link("b", 4, "c", 4)
    switches.append(b_to_c_2_v)

    b_to_d_1 = Cable()
    b_to_d_1_v = b_to_d_1.link("b", 5, "d", 3)
    switches.append(b_to_d_1_v)

    b_to_d_2 = Cable()
    b_to_d_1_v = b_to_d_2.link("b", 6, "d", 4)
    switches.append(b_to_d_1_v)

    c_to_d_1 = Cable()
    c_to_d_1_v = c_to_d_1.link("c", 5, "d", 5)
    switches.append(c_to_d_1_v)

    c_to_d_2 = Cable()
    c_to_d_2_v = c_to_d_2.link("c", 6, "d", 6)
    switches.append(c_to_d_2_v)

    for i in switches:
        for j in i:
            for obj in gc.get_objects():
                if isinstance(obj, Switch):
                    if obj.letter == j[0]:
                        obj.ports[j[1]] = "up"
    print(switch_a.ports)
    print(switch_b.ports)
    print(switch_c.ports)
    print(switch_d.ports)
