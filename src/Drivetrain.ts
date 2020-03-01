interface Controller {
    xbox: boolean;
    start: boolean;
    select: boolean;
    r_bumper: boolean;
    l_bumper: boolean;
    x: boolean;
    y: boolean;
    a: boolean;
    b: boolean;
    d_right: boolean;
    d_left: boolean;
    d_down: boolean;
    d_up: boolean;
    l_x: number;
    l_y: number;
    r_x: number;
    r_y: number;
    l_3: boolean;
    r_3: boolean;
    l_trigger: number;
    r_trigger: number;
}

enum DrivetrainState {
    Closed,
    Open,
}

const IDLECONTROLLER : Controller = {
    xbox: false,
    start: false,
    select: false,
    r_bumper: false,
    l_bumper: false,
    x: false,
    y: false,
    a: false,
    b: false,
    d_right: false,
    d_left: false,
    d_down: false,
    d_up: false,
    l_x: 0,
    l_y: 0,
    r_x: 0,
    r_y: 0,
    l_3: false,
    r_3: false,
    l_trigger: 0,
    r_trigger: 0,
}

class Drivetrain {
    state: DrivetrainState;
    controllerState: Controller;

    getControllerState() : Controller {
        if (this.state == DrivetrainState.Open) {
            return this.controllerState;
        } else {
            return IDLECONTROLLER;
        }
    }

    constructor() {
        this.state = DrivetrainState.Closed;
    }
}