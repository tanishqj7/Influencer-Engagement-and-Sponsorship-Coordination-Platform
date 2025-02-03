from flask import render_template_string, render_template, Flask, request, jsonify
from flask_security import auth_required, current_user, roles_required
from flask_security import SQLAlchemySessionUserDatastore
from flask_security.utils import hash_password

def create_views(app : Flask, user_datastore : SQLAlchemySessionUserDatastore, db ):

    # homepage
    @app.route('/')
    def home():
        return render_template('index.html') # entry point to vue frontend

    # profile
    @app.route('/profile')
    @auth_required('token', 'session')
    def profile():
        return render_template_string(
            """
                <h1> this is homepage </h1>
                <p> Welcome, {{current_user.email}}</p>
                <p> Role :  {{current_user.roles[0].description}}</p>
                <p><a href="/logout">Logout</a></p>
            """
        )

    @app.route('/register', methods=['POST'])
    def register():

        data = request.get_json()


        email = data.get('email')
        password = data.get('password')
        role = data.get('role')
 

        if not email or not password or not role:
            return jsonify({'message' : 'invalid input'}), 403

        if user_datastore.find_user(email = email ):
            return jsonify({'message' : 'user already exists'}), 400

        if role == 'Sponsor':
            user_datastore.create_user(email = email, password = hash_password(password), active = False, roles = ['sponsor'])
            db.session.commit()
            return jsonify({'message' : 'Sponsor succesfully created, waiting for admin approval'}), 201

        elif role == 'Influencer':
            try :
                user_datastore.create_user(email = email, password = hash_password(password), active = True, roles=['influencer']), 201
                db.session.commit()
            except:
                print('error while creating')
            return jsonify({'message' : 'Influencer successfully created'})

        return jsonify({'message' : 'invalid role'}), 400


    @app.route('/spon-dashboard')
    @roles_required('sponsor')
    def spon_dashboard():
        return render_template_string(
            """
                <h1>this is instructor dashboard</h1>
                <p>This should only be accessible to inst</p>
            """
        )
    
    @app.route('/influ-dashboard')
    @roles_required('influencer')
    def influ_dashboard():
        return render_template_string(
            """
                <h1>this is student dashboard</h1>
                <p>This should only be accessible to student</p>
            """
        )
    
    
    @app.route('/activate-sponsor/<id>' )
    @roles_required('admin')
    def activate_inst(id):

        user = user_datastore.find_user(id=id)
        if not user:
            return jsonify({'message' : 'user not present'}), 404

        # check if inst already activated
        if (user.active == True):
            return jsonify({'message' : 'user already active'}), 400

        user.active = True
        db.session.commit()
        return jsonify({'message' : 'user is activated'}), 200
    
    # # activate study resource
    # @app.route('/verify-resource/<id>')
    # @roles_required('inst')
    # def activate_resource(id):
    #     resource = StudyResource.query.get(id)
    #     if not resource:
    #         return jsonify({'message' : 'invalid id'}), 400
    #     resource.is_approved = True
    #     db.session.commit()
    #     return jsonify({'message' : 'resource is now approved'}), 200

    # # endpoint to get inactive inst
    # @app.route('/inactive_instructors', methods=['GET'])
    # @roles_required('admin')

    # def get_inactive_instructors():
    #     # Query for all users
    #     all_users = user_datastore.user_model().query.all()
        
    #     # Filter users to get only inactive instructors
    #     inactive_instructors = [
    #         user for user in all_users 
    #         if not user.active and any(role.name == 'inst' for role in user.roles)
    #     ]
        
    #     # Prepare the response data
    #     results = [
    #         {
    #             'id': user.id,
    #             'email': user.email,
    #         }
    #         for user in inactive_instructors
    #     ]
        
    #     return jsonify(results), 200