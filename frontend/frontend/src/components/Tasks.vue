<template>
    <div class="jumbotron vertical-center">
        <div class="container">
            <!-- bootswatch CDN -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css" integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
            <div class="row">
                <div class="col-sm-8">
                     <h2 class="text-center bg-primary text-white" style="border-radius: 10px;">Task's Library ✔</h2 >
                     <hr><br>

                     <!-- Alert Message -->
                     <b-alert variant="success" v-if="showMessage" show> {{ message }} </b-alert>

                     <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
                     <br><br>
                     <table class="table table-hover">
                        <!-- Table Head -->
                        <thead>
                            <tr>
                                <!-- Table header cells -->
                                <th scope="col">Title</th>
                                <th scope="col">Essence</th>
                                <th scope="col">Done?</th>
                                <th scope="col">To Update</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="task, index in tasks" :key="index">
                            <td>{{ task.title }}</td>
                            <td>{{ task.essence }}</td>
                            <td>
                                <span v-if="task.status">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-info btn-sm"
                                     v-b-modal.task-update-modal
                                     @click="editTask(task)">Update</button>
                                    <button type="button" class="btn btn-danger btn-sm" @click="deleteTask(task)">Delete</button>
                                </div>
                            </td>
                            </tr>
                        </tbody>
                     </table>
                    <footer class="bg-primary text-white text-center" style="border-radius: 8px;">Copyright &copy 2023 Gleb JUPYplus</footer>
                </div>
            </div>

        <!-- First Modal -->
        <b-modal ref="addTaskModal"
         id="task-modal" 
         title="Add a new task" 
         hide-backdrop hide-footer> 
   <b-form @submit="onSubmit" @reset="onReset" class="w-100"> 
   <b-form-group id="form-title-group"
                 label="Title:"
                 label-for="form-title-input">
     <b-form-input id="form-title-input"
                   type="text"
                   v-model="addTaskForm.title"
                   required
                   placeholder="Enter title">
     </b-form-input>
   </b-form-group>

   <b-form-group id="form-essence-group"
                 label="Essence:"
                 label-for="form-essence-input">
         <b-form-input id="form-essence-input"
                       type="text"
                       v-model="addTaskForm.essence"
                       required
                       placeholder="Enter essence">
       </b-form-input>
     </b-form-group>
     
     <b-form-group id="form-status-group">
        <div>
            <label for="myCheckbox" style="margin-right: 10px;">Done?</label>
            <input id="myCheckbox" type="checkbox" v-model="status" />
        </div>
     </b-form-group>  

              
              
            <!-- Buttons: submit and reset -->
            <b-button type="submit" variant="outline-info">Submit</b-button>
            <b-button type="reset" variant="outline-danger">Reset</b-button>

                    </b-form>  
        </b-modal>
<!-- End of Modal 1 -->

<!-- Second Modal -->
<b-modal ref="editTaskModal"
        id="task-update-modal"
        title="Update" hide-backdrop
        hide-footer>
   <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
   <b-form-group id="form-title-edit-group"
                 label="Title:"
                 label-for="form-title-edit-input">
     <b-form-input id="form-title-edit-input"
                   type="text"
                   v-model="editSingleTask.title"
                   required
                   placeholder="Enter title">
     </b-form-input>
   </b-form-group>

   <b-form-group id="form-essence-edit-group"
                 label="Essence:"
                 label-for="form-essence-edit-input">
         <b-form-input id="form-essence-edit-input"
                       type="text"
                       v-model="editSingleTask.essence"
                       required
                       placeholder="Enter essence">
       </b-form-input>
     </b-form-group>
     
     <b-form-group id="form-status-edit-group">
        <div>
            <label for="myCheckbox" style="margin-right: 10px;">Done?</label>
            <input id="myCheckbox" type="checkbox" v-model="editSingleTask.status" />
        </div>
     </b-form-group>

              
              
            <!-- Buttons: submit and reset -->

            <b-button type="submit" variant="outline-info">Update</b-button>
            <b-button type="reset" variant="outline-danger">Cancel</b-button>

                    </b-form>
        </b-modal>

<!-- End of Modal 2 -->

        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return{
            status: false,
            tasks: [],
            addTaskForm: {
                title: "",
                essence: "",
                status: false,
            },
            message : "",
            showMessage : false,
            editSingleTask: {
                title: "",
                essence: "",
                status: false,
            },
            };
        },
        mounted() {
                  document.title = "Tasks list RESTful";
                      }, 

        // GET function
        methods:{
            getTasks(){
                const path = 'https://todobackend-s44p.onrender.com/tasks';
                axios.get(path)
                .then((res) => {
                    this.tasks = res.data.tasks;
                    setTimeout(() => { 
                    this.showMessage = false;
                    }, 3000);
                })
                .catch((err) => {
                    console.error(err)
                });
            },
            // POST function
            addTask(payload) {
            const path = 'https://todobackend-s44p.onrender.com/tasks';
            axios.post(path, payload)
                .then(() => {
                this.getTasks();
                this.message = 'Task Added 👏';
                this.showMessage = true;
                })
                .catch((error) => {
                console.error(error);
                this.getTasks();
                });
            },
            initForm() {
                this.addTaskForm.title = "";
                this.addTaskForm.essence = "";
                this.addTaskForm.status = [];
                this.editSingleTask.id = '';
                this.editSingleTask.title = '';
                this.editSingleTask.genre = '';
                this.editSingleTask.status = [];
            },
            // This is for the first modal 
            onSubmit(e) {
                e.preventDefault();
                this.$refs.addTaskModal.hide();
                const payload = {
                    title: this.addTaskForm.title,
                    essence: this.addTaskForm.essence,
                    status: this.status, 
                };
                this.addTask(payload);
                this.initForm();
                },
            onReset(e){
                e.preventDefault(),
                this.$refs.addTaskModal.hide();
                this.initForm();
            },

            // This is for the second modal

            onSubmitUpdate(e){
                e.preventDefault();
                this.$refs.editTaskModal.hide();
                const payload = {
                    title: this.editSingleTask.title,
                    essence: this.editSingleTask.essence,
                    status: this.editSingleTask.status, 
                };
                this.updateTask(payload, this.editSingleTask.task_id)
            },
            // Handle cancel button click
            onResetUpdate(e){
                e.preventDefault();
                this.$refs.editTaskModal.hide();
                this.initForm();
                this.getTasks();

            },

            // Update Task
            updateTask(payload, task_id){
                const path = `https://todobackend-s44p.onrender.com/tasks/${task_id}`;
                axios.post(path, payload)
                .then(() => {
                    this.getTasks();
                    this.message = "Game updated ! ⚙️"
                    this.showMessage = true;
                })
                .catch((error) => {
                console.error(error);
                this.getTasks();
                });
            },
            // Delete Task
            removeTask(task){
                const path = `https://todobackend-s44p.onrender.com/tasks/${task['task_id']}`;
                axios.delete(path)
                .then(() => {
                    this.getTasks();
                    this.message = "Task Removed ! ♻️"
                    this.showMessage = true;
                })
                .catch((error) => {
                console.error(error);
                this.getTasks();
                });
            },
            // Handle Update Button
            editTask(task) {
               this.editSingleTask = task
            },
            // Handle delete button
            deleteTask(task){
                this.removeTask(task)
            },
        },
        created() {
            this.getTasks();
        },
    
}
</script>