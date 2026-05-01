export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;

    this.constructor._symbol = Symbol('cloneCar');
  }

  get brand() {
    return this._brand;
  }

  set brand(value) {
    this._brand = value;
  }

  get motor() {
    return this._motor;
  }

  set motor(value) {
    this._motor = value;
  }

  get color() {
    return this._color;
  }

  set color(value) {
    this._color = value;
  }

  cloneCar() {
    const Cls = this.constructor;
    const clone = new Cls();

    clone._brand = this._brand;
    clone._motor = this._motor;
    clone._color = this._color;

    return clone;
  }
}
