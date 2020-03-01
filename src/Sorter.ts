enum SorterState {
    Idle,
    Manual,
    HealingPotion,
    StrengthPotion,
    InvisibilityPotion,
}

class Sorter {
    state: SorterState;
    constructor() {
        this.state = SorterState.Idle;
    }
}