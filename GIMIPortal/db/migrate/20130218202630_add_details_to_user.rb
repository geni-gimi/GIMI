class AddDetailsToUser < ActiveRecord::Migration
  def change
    add_column :users, :username, :string
    add_column :users, :url, :string
  end
end
