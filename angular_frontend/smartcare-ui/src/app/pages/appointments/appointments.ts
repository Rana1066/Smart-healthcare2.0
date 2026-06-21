import { Component } from '@angular/core';
import { Navbar } from '../../components/navbar/navbar';
import { Appointment } from '../../services/appointment';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-appointments',
  imports: [CommonModule,Navbar],
  templateUrl: './appointments.html',
  styleUrl: './appointments.css',
})
export class Appointments {
appointments: any[] = [];

  constructor(
    private appointmentService: Appointment
  ) {}

  ngOnInit(): void {
    this.loadAppointments();
  }

  loadAppointments() {

    this.appointmentService
      .getAppointments()
      .subscribe({
        next: (data: any) => {
          this.appointments = data;
        },
        error: (error: any) => {
          console.log(error);
        }
      });
  }
}
