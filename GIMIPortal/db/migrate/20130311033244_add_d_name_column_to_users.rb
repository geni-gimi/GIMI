class AddDNameColumnToUsers < ActiveRecord::Migration
  def change
    add_column :users, :dname, :string
  end
end
