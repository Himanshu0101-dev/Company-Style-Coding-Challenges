use std::cmp::Reverse;
use std::collections::BinaryHeap;

#[derive(Debug)]
struct Slot {
    id: i32,
    distance: i32,
    available_from: i32,
}

fn assign_parking(
    slots: Vec<Slot>,
    vehicles: Vec<(i32, i32)>,
) -> Vec<(i32, i32)> {

    let mut slots = slots;
    slots.sort_by_key(|s| s.available_from);

    let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

    let mut i = 0;
    let mut result = Vec::new();

    for (vehicle_id, arrival) in vehicles {

        while i < slots.len()
            && slots[i].available_from <= arrival
        {
            heap.push(
                Reverse((
                    slots[i].distance,
                    slots[i].id
                ))
            );
            i += 1;
        }

        if let Some(Reverse((_d, slot_id))) = heap.pop() {
            result.push((vehicle_id, slot_id));
        } else {
            result.push((vehicle_id, -1));
        }
    }

    result
}

fn main() {
    let slots = vec![
        Slot { id:1, distance:20, available_from:2 },
        Slot { id:2, distance:10, available_from:1 },
        Slot { id:3, distance:15, available_from:3 },
        Slot { id:4, distance:10, available_from:2 },
    ];

    let vehicles = vec![
        (101,1),
        (102,2),
        (103,3),
        (104,4),
    ];

    println!("{:?}", assign_parking(slots, vehicles));
}
